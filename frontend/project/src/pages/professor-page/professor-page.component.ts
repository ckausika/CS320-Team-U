import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { MatPaginatorModule, PageEvent } from '@angular/material/paginator';
import { MatCardModule } from '@angular/material/card';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-professor-page',
  standalone: true,
  imports: [CommonModule, MatPaginatorModule, MatCardModule, MatIconModule, MatButtonModule],
  templateUrl: './professor-page.component.html',
  styleUrls: ['./professor-page.component.css']
})
export class ProfessorPageComponent implements OnInit {
  professors: any[] = [];
  visibleProfessors: any[] = [];

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.dataService.fetchProfessorData().subscribe(data => {
      this.professors = data.Data;
      this.updateVisibleProfessors(0, 15);
    });
  }

  changePage(event: PageEvent) {
    const startIndex = event.pageIndex * event.pageSize;
    const endIndex = startIndex + event.pageSize;
    this.updateVisibleProfessors(startIndex, endIndex);
  }

  private updateVisibleProfessors(startIndex: number, endIndex: number) {
    this.visibleProfessors = this.professors.slice(startIndex, endIndex);
  }

  goToLink(url: string) {
    window.open(url, "_blank");
  }
}
