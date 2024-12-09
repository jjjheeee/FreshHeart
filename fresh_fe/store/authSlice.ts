// store/authSlice.ts
import { createSlice } from "@reduxjs/toolkit";

const authSlice = createSlice({
    name: 'auth',
    initialState: {
      accessToken: null,
      isAuthenticated: false,
    },
    reducers: {
      setAccessToken: (state, action) => {
        state.accessToken = action.payload;
        state.isAuthenticated = !!action.payload;
      },
      logout: (state) => {
        state.accessToken = null;
        state.isAuthenticated = false;
      },
    },
  });
  
  export const { setAccessToken, logout } = authSlice.actions;
  export default authSlice.reducer;