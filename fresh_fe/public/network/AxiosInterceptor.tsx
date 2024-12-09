import axios, { AxiosError, AxiosInstance, AxiosResponse, InternalAxiosRequestConfig } from "@/node_modules/axios/index";
import { setAccessToken, logout } from "../../store/authSlice"
import { useDispatch } from 'react-redux';
import { useRouter } from "@/node_modules/next/router";
import { useRef, useEffect } from "react";
import { getCookie } from "../utils/setToken";
import { handleLogout } from "../utils/functions";

//axios instance
export const axiosInstance = axios.create({
    baseURL: "http://localhost:8000/api",
    // baseURL: process.env.AXIOS_BASE_URL,
    withCredentials: true,
});
  
const generalAxiosInstance = axios.create({
    withCredentials: true,
});
  
//redux-persist에서 accessToken 취득
export const getAccessToken = async () => {
    const storedAccessToken = sessionStorage.getItem('persist:root');

    if (storedAccessToken) {
        const tokenObj = JSON.parse(storedAccessToken);
        const accessToken = JSON.parse(tokenObj.access).accessToken;
        return accessToken;
    } else {
        return '토큰 파싱 실패';
    }
};
  
const getStatusToken = async () => {
    return sessionStorage.getItem('statusToken');
}

//axios Components
const AxiosInterceptors: React.FC<{ children: React.ReactNode }> = ({
    children,
  }) => {
    const dispatch = useDispatch();
    const router = useRouter();
  
    const isRefreshingToken = useRef(false);
    const isLogoutHandled = useRef(false);
  
    useEffect(() => {
      // request interceptors
      axiosInstance.interceptors.request.use(
        async (config) => {
          // request 전달전에 작업 수행 => request header에 access token을 넣어준다.
          const accessToken = await getAccessToken();
          const statusToken = await getStatusToken();
          if (accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`;
          }
          if (statusToken) {
            config.headers['Status-Token'] = statusToken; 
          }
          return config;
        },
        (error) => {
          return Promise.reject(error);
        },
      );
  
      // response interceptors
      axiosInstance.interceptors.response.use(
        (response) => {
          // 2xx 번대 정상 응답시 그대로 작업 수행
          return response;
        },
        async (error) => {
          // 2xx 범위 외에 있는 코드 응답시 해당 함수 트리거
          const originalRequest = error.config;
          const refreshToken = getCookie('refreshToken');
  
          if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            if (!isRefreshingToken.current) {
              isRefreshingToken.current = true;
              try {
                const response = await generalAxiosInstance.post('/api/users/token/refresh', { refresh: refreshToken });
                if (response.status === 200) {
                  const newAccessToken = response.data.access;
                  dispatch(setAccessToken(newAccessToken));
                  originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
                  return axiosInstance(originalRequest);
                } else {
                  handleLogout(dispatch, false, null);
                  alert('로그인이 만료되었습니다. 다시 로그인해주세요.');
                  router.push('/login');
                }
              } catch (refreshError: any) {
                handleLogout(dispatch, false, null);
                alert('로그인이 만료되었습니다. 다시 로그인해주세요.');
                router.push('/login');
              } finally {
                isRefreshingToken.current = false;
              }
            }
          } else if (error.response.status === 409) {
            if (!isLogoutHandled.current) {
              isLogoutHandled.current = true;
              handleLogout(dispatch, false, null);
              alert('중복 로그인으로 인해 로그아웃됩니다.');
              router.push('/login?option=duplicate');
            }
          }
          return Promise.reject(error);
        },
      );
    }, [dispatch, router]);
  
    return <>{children}</>;
  };

  export default AxiosInterceptors;