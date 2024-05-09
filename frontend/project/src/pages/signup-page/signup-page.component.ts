import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { DataService } from '../../services/data.service';
import { jwtDecode } from 'jwt-decode';

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
  loading = false;

  constructor(private dataService: DataService, private router: Router) {}

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
      this.loading = true;
      this.dataService.signUp(payload).subscribe({
        next: (value) => {
          this.loading = false;
          if (value.Token) {
            this.dataService.user = jwtDecode(value.Token);
            this.router.navigate(['']);
          } else {
            this.error = value.ErrorMessage;
            console.log(value.Error)
          }
        },
        error: (err) => {
          this.loading = false;
          this.error = "Server error.";
          console.log(err);
        }
      });
    }
  }
}
