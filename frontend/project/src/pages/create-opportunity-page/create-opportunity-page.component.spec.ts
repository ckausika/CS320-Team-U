import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateOpportunityPageComponent } from './create-opportunity-page.component';

describe('CreateOpportunityPageComponent', () => {
  let component: CreateOpportunityPageComponent;
  let fixture: ComponentFixture<CreateOpportunityPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CreateOpportunityPageComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CreateOpportunityPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
