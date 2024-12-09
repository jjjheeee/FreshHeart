import { createSlice, PayloadAction } from "@reduxjs/toolkit";

interface User {
  // userId: number;
  email: string;
  nickname: string;
//   userThumbnail: string;
  isLogin: boolean;
//   isMentor: boolean;
//   isSocialLogin: boolean;
//   mentorName: string;
}

interface UserState {
  user: User;
}

const initialState: UserState = {
  user: {
    // userId: 0,
    email: '',
    nickname: '',
    // userThumbnail: '',
    isLogin: false,
    // isMentor: false,
    // isSocialLogin: false,
    // mentorName: '',
  }
}

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    setUser: (state:any, action: PayloadAction<User>) => { state.user = action.payload }, // 로그인
    initUser: (state:any) => { state.user = initialState.user }, // 로그아웃
    changeNickname: (state:any, action: PayloadAction<string>) => { state.user.userNickname = action.payload }, // 닉네임 변경
    // changeThumbnail: (state, action: PayloadAction<string>) => { state.user.userThumbnail = action.payload }, // 프로필 사진 변경
  }
})

export const { setUser, initUser, changeNickname } = userSlice.actions;
export default userSlice;