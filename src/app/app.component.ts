import { Component } from '@angular/core';
import { IResearcher } from './researchers';
import people from '../assets/researchers.json';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Egyptians in AI';
  researchers: IResearcher[] = this.shuffle(people);

  constructor() { }

  ngOnInit(): void { }

  shuffle(array: any[]): any[] {
    return array.sort(() => Math.random() - 0.5);
  }

  sortAZ() {
    this.researchers = people.sort((a, b) => a.name.localeCompare(b.name));
  }

  sortHIndex() {
    this.researchers = people.sort((a, b) => b.hindex - a.hindex);
  }

  sortShuffle() {
    this.researchers = this.shuffle(this.researchers);
  }
  
}
