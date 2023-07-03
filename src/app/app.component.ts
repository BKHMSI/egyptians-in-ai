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
  profiles = this.researchers;
  rinterestsFreq: {[key: string]: number} = {};
  rinterests = this.getResearchIntersts(people);
  searchQuery = "";

  constructor() { }

  ngOnInit(): void { }

  getResearchIntersts(people: IResearcher[]): {[key: string]: boolean} {
    let interests = new Set<string>();
    let interestsFreq: {[key: string]: number} = {}
    for(let i = 0; i<people.length; i++){
      for(let j = 0; j<people[i].interests.length; j++){
        let curr = people[i].interests[j];
        interestsFreq[curr] = (interestsFreq[curr] || 0) + 1;
        interests.add(curr)
      }
    }

    this.rinterestsFreq = interestsFreq;

    let interestsArr = Array.from(interests).sort();
    let interestsMap: {[key: string]: boolean} = {}
    for(let i = 0; i<interests.size; i++){
      interestsMap[interestsArr[i]] = true;
    }
    
    return interestsMap;
  }

  shuffle(array: any[]): any[] {
    return array.sort(() => Math.random() - 0.5);
  }

  sortAZ() {
    this.researchers = people.sort((a, b) => a.name.localeCompare(b.name));
  }

  sortHIndex() {
    this.researchers = people.sort((a, b) => b.hindex - a.hindex);
  }
  
  sortCitations() {
    this.researchers = people.sort((a, b) => b.citedby - a.citedby);
  }

  sortShuffle() {
    this.researchers = this.shuffle(this.researchers);
  }

  filterProfiles(event:any) {
    let query:string = event.target.value.toLowerCase();
    this.researchers = this.profiles;

    if(query.trim() == ""){
      this.researchers = this.profiles;
      return;
    }

    let filtered:IResearcher[] = []
    for(let i = 0; i<this.researchers.length; i++){
      if(this.researchers[i].name.toLowerCase().includes(query)){
        filtered.push(this.researchers[i]);
      }
    }

    this.researchers = filtered;
  }

  filterInterests() {
    this.researchers = this.profiles;
    let filtered:IResearcher[] = []
    for(let i = 0; i<this.researchers.length; i++){
      for(let key in this.rinterests){
        if(this.rinterests[key] && this.researchers[i].interests.includes(key)){
          filtered.push(this.researchers[i]);
          break;
        }
      }
    }
    this.researchers = filtered;
  }

  checkAllInterests() {
    for (let key in this.rinterests) {
      this.rinterests[key] = true;
    }
    this.researchers = this.profiles;
  }  

  clearAllInterests() {
    for (let key in this.rinterests) {
      this.rinterests[key] = false;
    }
    this.researchers = this.profiles;
  }

}
