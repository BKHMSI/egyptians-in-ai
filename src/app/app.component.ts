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
  researchers: IResearcher[] = people.sort((a, b) => b.hindex - a.hindex);

  constructor() { }

  ngOnInit(): void { }
}
