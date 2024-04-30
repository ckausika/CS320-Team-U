import { Component } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule, MatFormField} from '@angular/material/form-field';
import {MatButtonModule} from '@angular/material/button';
import {MatDividerModule} from '@angular/material/divider';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-create-opportunity-page',
  standalone: true,
  imports: [RouterLink, MatCardModule, MatInputModule, MatFormFieldModule, MatButtonModule, MatDividerModule,MatFormField],
  templateUrl: './create-opportunity-page.component.html',
  styleUrl: './create-opportunity-page.component.css'
})
export class CreateOpportunityPageComponent {

}
