import { Routes } from '@angular/router';
import {HomePageComponent} from '../pages/home-page/home-page.component'
import {LoginPageComponent} from '../pages/login-page/login-page.component'
import {SignUpPageComponent} from '../pages/signup-page/signup-page.component'
import {PageNotFoundComponent} from '../pages/page-not-found/page-not-found.component'
import {ResearchPageComponent} from '../pages/research-page/research-page.component'
import {ApplicationPageComponent} from '../pages/application-page/application-page.component'
import {CreateOpportunityPageComponent} from '../pages/create-opportunity-page/create-opportunity-page.component'
import {HelpPageComponent} from '../pages/help-page/help-page.component';
import {ProfessorPageComponent} from '../pages/professor-page/professor-page.component';


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
        path: 'signup',
        title: 'Sign Up Page',
        component: SignUpPageComponent
    },
    {
        path: 'research',
        title: 'Research Page',
        component: ResearchPageComponent
    },
    {
        path: 'professor',
        title: 'Professor Page',
        component: ProfessorPageComponent
    },
    {
        path: 'application',
        title: 'Application Page',
        component: ApplicationPageComponent
    },
    {
        path: 'create-opportunity',
        title: 'Create Opportunity Page',
        component: CreateOpportunityPageComponent
    },
    {
        path: 'help',
        title: 'Help Page',
        component: HelpPageComponent
    },
    {
        path: '**',
        title: 'Page Not Found',
        component: PageNotFoundComponent
    },
];