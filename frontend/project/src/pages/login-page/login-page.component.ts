import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatButtonModule} from '@angular/material/button';
import {MatDividerModule} from '@angular/material/divider';

@Component({
  selector: 'app-login-page',
  standalone: true,
  imports: [RouterLink, MatCardModule, MatInputModule, MatFormFieldModule, MatButtonModule, MatDividerModule],
  templateUrl: './login-page.component.html',
  styleUrl: './login-page.component.css'
})
export class LoginPageComponent {
  hide = true;
}
