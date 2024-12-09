import { Cookies } from "@/node_modules/react-cookie/cjs/index";

const cookies = new Cookies();

export const setCookie = (name: string, value: string, options?: any) => {
  if (typeof document !== 'undefined') {
    return cookies.set(name, value, { ...options });
  }
}

export const getCookie = (name: string) => {
  if (typeof document !== 'undefined') {
    return cookies.get(name);
  }
}

export const removeCookie = (name: string, options?: any) => {
  if (typeof document !== 'undefined') {
    return cookies.remove(name, { ...options });
  }
};