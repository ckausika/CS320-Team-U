import { Component } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule, MatFormField} from '@angular/material/form-field';
import {MatButtonModule} from '@angular/material/button';
import {MatDividerModule} from '@angular/material/divider';
import { RouterLink} from '@angular/router';
import { FormControl, ReactiveFormsModule, FormGroup } from '@angular/forms';
import { DataService } from '../../services/data.service';

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

  constructor(private dataService: DataService) {}
  getFormInfo() {
    this.dataService.submitOpp(this.createOppForm);
  }
}


