export interface UserInfo {
    email: string,
    nickname: string,
    isLogin: boolean
}

export interface receiveEmpathy{
    like:number,
    cheerUp:number
}

export interface Sympathy {
    emotionTag: string,
    title: string,
    description: string,
    receiveEmpathy:receiveEmpathy
}