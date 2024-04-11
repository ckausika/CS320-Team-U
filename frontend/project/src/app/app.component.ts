import { Component } from '@angular/core';
import { RouterOutlet, RouterLink, Router, NavigationEnd } from '@angular/router';
import {MatIconModule} from '@angular/material/icon';
import {MatDividerModule} from '@angular/material/divider';
import {MatButtonModule} from '@angular/material/button';
import { NgIf } from '@angular/common';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [NgIf, RouterOutlet, RouterLink, MatButtonModule, MatDividerModule, MatIconModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'research-finder';
  showNavbar: boolean;

  constructor(private router: Router) {
    this.showNavbar = this.router.url !== '/login';

    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        this.showNavbar = event.url !== '/login';
      }
    });
  }
}
