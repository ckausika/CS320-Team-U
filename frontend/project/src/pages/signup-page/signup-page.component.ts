import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatButtonModule} from '@angular/material/button';
import {MatDividerModule} from '@angular/material/divider';

@Component({
  selector: 'app-signup-page',
  standalone: true,
  imports: [RouterLink, MatCardModule, MatInputModule, MatFormFieldModule, MatButtonModule, MatDividerModule],
  templateUrl: './signup-page.component.html',
  styleUrl: './signup-page.component.css'
})
export class SignUpPageComponent {
  hide = true;
}
