import { Component } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';
import { HttpClient, HttpParams } from '@angular/common/http';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatDividerModule } from '@angular/material/divider';
import { NgIf } from '@angular/common';
import { Observable, catchError, throwError } from 'rxjs';
import { Parameter } from '../models/requests'


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [NgIf, RouterOutlet, RouterLink, MatToolbarModule, MatButtonModule, MatDividerModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'research-finder';

  data: any;
  gets: any;

  readonly ROOT_URL = 'http://localhost:5000/api'
  constructor(private http: HttpClient) {

  }

  get(endpoint: string, parameters?: Parameter[]): Observable<any> {
    let params = new HttpParams();
    if (parameters) {
      parameters.forEach((parameter) => {
        params = params.set(parameter.param, parameter.value);
      });
    }
    return this.http.get(`${this.ROOT_URL}/get${endpoint}`, {params}).pipe(
      catchError((error) => {
        console.error('Error making HTTP request', error);
        return error;
      })
    );
  }

  fetchLabData() {
    const params = [{param: 'name', value: ''}];
    this.get('/lab', params).subscribe({
      next: (data) => {
        this.data = data;
        console.log('Received data:', data);
      },
      error: (error) => console.error('Failed to fetch data:', error)
    });
  }
}
