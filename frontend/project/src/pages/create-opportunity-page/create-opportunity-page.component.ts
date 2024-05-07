import { Component } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule, MatFormField} from '@angular/material/form-field';
import {MatButtonModule} from '@angular/material/button';
import {MatDividerModule} from '@angular/material/divider';
import { RouterLink } from '@angular/router';
import { FormControl, ReactiveFormsModule, FormGroup } from '@angular/forms';
import { HttpClientModule, HttpClient} from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';

@Component({
  selector: 'app-create-opportunity-page',
  standalone: true,
  imports: [RouterLink, MatCardModule, MatInputModule, MatFormFieldModule, MatButtonModule, MatDividerModule,MatFormField, ReactiveFormsModule],
  templateUrl: './create-opportunity-page.component.html',
  styleUrl: './create-opportunity-page.component.css'
})

export class CreateOpportunityPageComponent {
  createOppForm = new FormGroup({
    yourTitle : new FormControl(''),
    firstName : new FormControl(''),
    lastName : new FormControl(''),
    emailAddress : new FormControl(''),
    jobTitle : new FormControl(''),
    expectedHours : new FormControl(''),
    location : new FormControl(''),
    jobDescription : new FormControl(''),
  });
  
  readonly ROOT_URL = 'http://localhost:5000/api'
  constructor(private http: HttpClient) {

  }
  getFormInfo():Observable<any> {
    console.log(this.createOppForm.value) // LETS GOOOOO IT WORKED WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    // CHECK FOR NULL VALUES AND CHECK VALIDATION --> CHECK DOCS FOR HOW TO VALIDATE, BUT FOR NOW
    return this.http.post(`${this.ROOT_URL}/put/opp-form`,this.createOppForm.value).pipe(
      catchError((error) => {
        console.error('Error making HTTP request', error);
        return error;
      })
    )
  }
}


