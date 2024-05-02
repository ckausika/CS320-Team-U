import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-signup-page',
  standalone: true,
  imports: [RouterLink, MatCardModule, MatInputModule, MatFormFieldModule, MatButtonModule, MatButtonToggleModule, FormsModule],
  templateUrl: './signup-page.component.html',
  styleUrl: './signup-page.component.css'
})
export class SignUpPageComponent {
  hide = true;
  username = '';
  email = '';
  password = '';
  rePassword = '';
  role = '';
  error = '';

  constructor(private dataService: DataService) {}

  signup() {
    if (!this.username) {
      this.error = "Please enter a username";
    } else if (!this.email) {
      this.error = "Please enter an email";
    } else if (!this.password) {
      this.error = "Please enter a password";
    } else if (!this.rePassword) {
      this.error = "Please re-enter your password";
    } else if (this.password !== this.rePassword) {
      this.error = "Passwords must match";
    } else if (!this.role) {
      this.error = "Please select a role";
    } else {
      const payload = {
        username: this.username,
        email: this.email,
        password: this.password,
        role: this.role
      };
      console.log(payload);
      console.log(this.dataService.signUp(payload));
    }
  }
}
