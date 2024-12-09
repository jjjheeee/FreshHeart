import { configureStore, combineReducers } from "@reduxjs/toolkit";
import storage from "redux-persist/lib/storage";
import logger from "redux-logger";
import persistReducer from "redux-persist/es/persistReducer";
import { persistStore } from 'redux-persist';  // persistStore 추가
import userSlice from "./user";

const reducers = combineReducers({
  user: userSlice.reducer,
})

const persistConfig = {
  key: "root",
  storage,
  whitelist: ["user"],  // "poppingUser"를 "user"로 변경
}

const persistedReducer = persistReducer(persistConfig, reducers);

const middleware = (getDefaultMiddleware: any) =>
  process.env.NODE_ENV !== 'production' ?
    getDefaultMiddleware({ serializableCheck: false }).concat(logger) :
    getDefaultMiddleware({ serializableCheck: false });

const store = configureStore({
  reducer: persistedReducer,
  middleware,
  devTools: process.env.NODE_ENV !== 'production',
});

export const persistor = persistStore(store);  // persistor 추가
export default store;