export interface Parameter {
    param: string;
    value: string;
}

export interface SignUpInput {
    username: string;
    email: string;
    password: string;
    role : any | "Professor"
}

export interface LogInInput {
    username: string;
    password: string;
}