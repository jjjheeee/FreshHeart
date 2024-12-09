import { setAccessToken, logout } from "../../store/authSlice"
import { initUser } from "@/store/user";
import { removeCookie } from '@/public/utils/setToken';

export const getKoreanYear = () => {
  const koreaTime = new Date().toLocaleString('en-US', {
    timeZone: 'Asia/Seoul',
  });
  const koreanDate = new Date(koreaTime);
  
  return koreanDate.getFullYear();
};

export const PriceFormatterPlusWon = (price: number) => {
  if (price){
    return price.toLocaleString('ko-KR') + '  원';
  }
};

export const PriceFormatter = (price: number) => {
  if (price){
    return price.toLocaleString('ko-KR');
  }
};

export const handleLogout = (dispatch: any, isClick: boolean = true, router: any = null) => {
  removeCookie('refreshToken');
  dispatch(initUser());
  dispatch(setAccessToken(''));
  localStorage.clear();
  sessionStorage.clear();
  if (isClick) {
    alert('정상적으로 로그아웃되었습니다. 이용해주셔서 감사합니다.')
    router.push('/users/signin')
  }
};

