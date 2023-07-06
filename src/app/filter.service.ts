import { Injectable } from '@angular/core';
import { IResearcher } from './researchers';

@Injectable({
  providedIn: 'root'
})

export class FilterService {

  constructor() { }

  getResearchIntersts(people: IResearcher[]): [{[key: string]: boolean}, {[key: string]: number}] {
    let interests = new Set<string>();
    let interestsFreq: {[key: string]: number} = {}
    for(let i = 0; i<people.length; i++){
      for(let j = 0; j<people[i].interests.length; j++){
        let curr = people[i].interests[j];
        interestsFreq[curr] = (interestsFreq[curr] || 0) + 1;
        interests.add(curr)
      }
    }

    let interestsArr = Array.from(interests).sort();
    let interestsMap: {[key: string]: boolean} = {}
    for(let i = 0; i<interests.size; i++){
      interestsMap[interestsArr[i]] = true;
    }
    
    return [interestsMap, interestsFreq];
  }

  filterProfiles(query:string, profiles: IResearcher[]): IResearcher[] {
    let researchers = profiles;

    if(query.trim() == ""){
      return profiles;
    }

    let filtered:IResearcher[] = []
    for(let i = 0; i<researchers.length; i++){
      if(researchers[i].name.toLowerCase().includes(query)){
        filtered.push(researchers[i]);
      }
    }

    return filtered;
  }

  filterInterests(profiles: IResearcher[], rinterests: {[key: string]: boolean}): IResearcher[] {
    let filtered:IResearcher[] = []
    for(let i = 0; i<profiles.length; i++){
      for(let key in rinterests){
        if(rinterests[key] && profiles[i].interests.includes(key)){
          filtered.push(profiles[i]);
          break;
        }
      }
    }
    return filtered;
  }

  shuffle(array: any[]): any[] {
    return array.sort(() => Math.random() - 0.5);
  }

  sortAZ(people: IResearcher[]) {
    return people.sort((a, b) => a.name.localeCompare(b.name));
  }

  sortHIndex(people: IResearcher[]) {
    return people.sort((a, b) => b.hindex - a.hindex);
  }
  
  sortCitations(people: IResearcher[]) {
    return people.sort((a, b) => b.citedby - a.citedby);
  }

  sortShuffle(people: IResearcher[]) {
    return this.shuffle(people);
  }
}
