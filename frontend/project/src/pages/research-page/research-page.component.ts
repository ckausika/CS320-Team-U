import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule, MatFormField} from '@angular/material/form-field';
import {MatButtonModule} from '@angular/material/button';
import {MatDividerModule} from '@angular/material/divider';
import { RouterLink } from '@angular/router';
import {MatPaginatorModule, PageEvent} from '@angular/material/paginator';
import { DataService } from '../../services/data.service';
import { SharedService } from '../../services/shared.service';

@Component({
  selector: 'app-research-page',
  standalone: true,
  imports: [CommonModule, RouterLink, MatCardModule, MatInputModule, MatFormFieldModule, MatButtonModule, MatDividerModule,MatFormField, MatPaginatorModule],
  templateUrl: './research-page.component.html',
  styleUrl: './research-page.component.css'
})
export class ResearchPageComponent {
  opportunity: any[] = [];
  visibleOpportunity: any[] = [];
  currentOpportunity:any
  isLoading = false;
  message:any;

  constructor(private dataService: DataService, private shared: SharedService) {}

  ngOnInit() {
    this.isLoading = true;
    this.dataService.fetchProfessorData().subscribe(data => {
      this.opportunity = data.Data;
      this.updateVisibleOpportunity(0, 6);
      this.isLoading = false;
    });
    this.updateVisibleOpportunity(0, 6);
     this.visibleOpportunity.length !== 0 ? this.currentOpportunity = this.visibleOpportunity[0]: this.currentOpportunity = "NA"
  }

  changePage(event: PageEvent) {
    const startIndex = event.pageIndex * event.pageSize;
    const endIndex = startIndex + event.pageSize;
    this.updateVisibleOpportunity(startIndex, endIndex);
  }

  private updateVisibleOpportunity(startIndex: number, endIndex: number) {
    this.visibleOpportunity = this.opportunity.slice(startIndex, endIndex);
  }

  newMessage(){
    this.shared.changeMessage(this.currentOpportunity);
  }

  setOpportunity(opp: any){
    this.currentOpportunity = opp;
  }

}
