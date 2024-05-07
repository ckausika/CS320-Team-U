export interface User {
    user: UserData;
    credential: string;
}

export interface UserData {
    username: string;
    email: string;
    role: string;
}