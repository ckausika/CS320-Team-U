import { Routes } from '@angular/router';
import {HomePageComponent} from '../pages/home-page/home-page.component'
import {LoginPageComponent} from '../pages/login-page/login-page.component'
import {PageNotFoundComponent} from '../pages/page-not-found/page-not-found.component'


export const routes: Routes = [
    {
        path: '',
        title: 'Home Page',
        component: HomePageComponent
    },
    {
        path: 'login',
        title: 'Login Page',
        component: LoginPageComponent
    },
    {
        path: '**',
        title: 'Page Not Found',
        component: PageNotFoundComponent
    },
];