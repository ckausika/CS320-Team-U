import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import {MatIconModule} from '@angular/material/icon';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {FormsModule} from '@angular/forms';
import { MatPaginatorModule, PageEvent } from '@angular/material/paginator';
import { MatCardModule } from '@angular/material/card';
import {MatButtonModule} from '@angular/material/button';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-professor-page',
  standalone: true,
  imports: [CommonModule, MatIconModule, MatInputModule, MatFormFieldModule, FormsModule, MatPaginatorModule, MatCardModule, MatButtonModule, MatProgressSpinnerModule],
  templateUrl: './professor-page.component.html',
  styleUrls: ['./professor-page.component.css']
})
export class ProfessorPageComponent implements OnInit {
  professors: any[] = [];
  visibleProfessors: any[] = [];
  isLoading = false;

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.isLoading = true;
    this.dataService.fetchProfessorData().subscribe(data => {
      this.professors = data.Data;
      this.updateVisibleProfessors(0, 10);
      this.isLoading = false;
    });
  }

  onSearch(value: string) {
    this.isLoading = true;
    this.dataService.fetchProfessorData([{ param: 'name', value: value }]).subscribe(data => {
      this.professors = data.Data;
      this.updateVisibleProfessors(0, 10);
      this.isLoading = false;
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
