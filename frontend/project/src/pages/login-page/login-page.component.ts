import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatButtonModule} from '@angular/material/button';
import {MatDividerModule} from '@angular/material/divider';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-login-page',
  standalone: true,
  imports: [RouterLink, MatCardModule, MatInputModule, MatFormFieldModule, MatButtonModule, MatDividerModule, FormsModule],
  templateUrl: './login-page.component.html',
  styleUrl: './login-page.component.css'
})
export class LoginPageComponent {
  hide = true;
  username = '';
  password = '';
  error = '';

  constructor(private dataService: DataService) {}

  login() {
    if (!this.username) {
      this.error = "Please enter a username";
    } else if (!this.password) {
      this.error = "Please enter a password";
    } else {
      const payload = {
        username: this.username,
        password: this.password,
      };
      console.log(this.dataService.logIn(payload));
    }
  }
}
