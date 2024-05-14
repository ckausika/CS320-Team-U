import { Component } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule, MatFormField} from '@angular/material/form-field';
import {MatButtonModule} from '@angular/material/button';
import {MatDividerModule} from '@angular/material/divider';
import { RouterLink } from '@angular/router';
import { FormControl, ReactiveFormsModule, FormGroup } from '@angular/forms';
import { DataService } from '../../services/data.service';
import { SharedService } from '../../services/shared.service';

@Component({
  selector: 'app-application-page',
  standalone: true,
  imports: [RouterLink, MatCardModule, MatInputModule, MatFormFieldModule, MatButtonModule, MatDividerModule,MatFormField, ReactiveFormsModule],
  templateUrl: './application-page.component.html',
  styleUrl: './application-page.component.css'
})
export class ApplicationPageComponent {
  createAppForm = new FormGroup({
    firstName : new FormControl(''),
    lastName : new FormControl(''),
    emailAddress : new FormControl(''),
    major : new FormControl(''),
    phoneNumber : new FormControl(''),
    gradDate : new FormControl(''),
    comments : new FormControl(''),
  });
  fileName=""
  message:any;
  constructor(private dataService: DataService, private shared: SharedService) {}
  getFormInfo() {
    this.dataService.submitOpp(this.createAppForm);
  }
  onFileSelected(event: any) {

    const file:File = event.target.files[0];

    if (file) {
        this.fileName = file.name;

        const formData = new FormData();

        formData.append("file", file);
    }
  
  }
  ngOnInit(){
    this.shared.currentMessage.subscribe(message => this.message = message);
  }
}
