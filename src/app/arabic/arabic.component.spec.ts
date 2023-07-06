import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ArabicComponent } from './arabic.component';

describe('ArabicComponent', () => {
  let component: ArabicComponent;
  let fixture: ComponentFixture<ArabicComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ArabicComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ArabicComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
