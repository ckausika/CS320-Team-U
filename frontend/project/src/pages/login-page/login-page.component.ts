import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatButtonModule} from '@angular/material/button';
import {MatDividerModule} from '@angular/material/divider';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { DataService } from '../../services/data.service';
import { jwtDecode } from 'jwt-decode';

@Component({
  selector: 'app-login-page',
  standalone: true,
  imports: [RouterLink, MatCardModule, MatInputModule, MatFormFieldModule, MatButtonModule, MatDividerModule, FormsModule, MatProgressSpinnerModule],
  templateUrl: './login-page.component.html',
  styleUrl: './login-page.component.css'
})
export class LoginPageComponent {
  hide = true;
  username = '';
  password = '';
  error = '';
  loading = false;

  constructor(private dataService: DataService, private router: Router) {}

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
      this.loading = true;
      this.dataService.logIn(payload).subscribe({
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
