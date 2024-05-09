import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { jwtDecode } from "jwt-decode";
import { Observable, catchError } from 'rxjs';
import { SignUpInput, Parameter, LogInInput } from '../models/requests';
import { User } from '../models/user';
import { FormGroup } from '@angular/forms';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private readonly ROOT_URL = 'http://localhost:5000/api';
  labs: any[] = [];
  professors: any[] = [];
  user: User | undefined;

  constructor(private http: HttpClient) {}

  get(endpoint: string, parameters?: Parameter[]): Observable<any> {
    let params = new HttpParams();
    if (parameters) {
      parameters.forEach((parameter) => {
        params = params.set(parameter.param, parameter.value);
      });
    }
    return this.http.get(`${this.ROOT_URL}/get${endpoint}`, { params }).pipe(
      catchError((error) => {
        console.error('Error making HTTP request', error);
        return error;
      })
    );
  }

  post(endpoint: string, body: any): Observable<any> {
    return this.http.post(`${this.ROOT_URL}${endpoint}`, body).pipe(
      catchError((error) => {
        console.error('Error making HTTP request', error);
        return error;
      })
    );
  }

  fetchLabData(params?: Parameter[]) {
    if (!params) {
      params = [{ param: 'name', value: '' }];
    }
    const obs = this.get('/lab', params);
    obs.subscribe({
      next: (data) => {
        this.labs = data.Data;
      },
      error: (error) => console.error('Failed to fetch data:', error)
    });
    return obs;
  }

  fetchProfessorData(params?: Parameter[]) {
    if (!params) {
      params = [{ param: 'name', value: '' }];
    }
    const obs = this.get('/professor', params);
    obs.subscribe({
      next: (data) => {
        this.professors = data.Data;
      },
      error: (error) => console.error('Failed to fetch data:', error)
    });
    return obs;
  }

  signUp(payload: SignUpInput) {
    const obs = this.post('/auth/createaccount', payload);
    obs.subscribe({
      next: (data) => {
        this.user = {credential: data.Token, user: jwtDecode(data.Token)};
      },
      error: (error) => console.error('Failed to fetch data:', error)
    });
    return obs;
  }

  logIn(payload: LogInInput) {
    const obs = this.post('/auth/login', payload);
    obs.subscribe({
      next: (data) => {
        this.user = {credential: data.Token, user: jwtDecode(data.Token)};
      },
      error: (error) => console.error('Failed to fetch data:', error)
    });
    return obs;
  }

  submitOpp(payload: FormGroup) {
    this.post('/post/create/opportunity', payload);
  }

  submitApp(payload:FormGroup) {
    this.post('/post/create/application',payload);
  }

}
