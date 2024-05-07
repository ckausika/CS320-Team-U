import { Component, OnInit } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';
import { HttpClient, HttpParams } from '@angular/common/http';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatDividerModule } from '@angular/material/divider';
import { NgIf } from '@angular/common';
import { MatMenuModule } from '@angular/material/menu';
import { ProfessorPageComponent } from '../pages/professor-page/professor-page.component';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [MatMenuModule, NgIf, RouterOutlet, RouterLink, MatToolbarModule, MatButtonModule, MatDividerModule, ProfessorPageComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'research-finder';

  constructor(public dataService: DataService) {}

  ngOnInit() {
    this.dataService.fetchLabData();
    this.dataService.fetchProfessorData();
  }
}