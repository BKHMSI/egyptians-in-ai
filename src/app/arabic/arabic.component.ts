import { Component, OnInit } from '@angular/core';
import { IResearcher } from '../researchers';
import people from '../../assets/researchers_ar.json';
import { FilterService } from '../filter.service';
@Component({
  selector: 'app-arabic',
  templateUrl: './arabic.component.html',
  styleUrls: ['./arabic.component.css']
})
export class ArabicComponent implements OnInit {

  title = 'المصريين  في الذكاء الاصطناعي';
  researchers: IResearcher[] = people;
  rinterests: {[key: string]: boolean} = {};
  rinterestsFreq: {[key: string]: number} = {};
  profiles = this.researchers;
  searchQuery = "";
  en_active: boolean = true;

  constructor(private filterService: FilterService) {
    [this.rinterests, this.rinterestsFreq] = this.filterService.getResearchIntersts(people);
    this.sortShuffle();
   }

  ngOnInit(): void {
  }

  sortAZ() {
    this.researchers = this.filterService.sortAZ(people);
  }

  sortHIndex() {
    this.researchers = this.filterService.sortHIndex(people);
  }
  
  sortCitations() {
    this.researchers = this.filterService.sortCitations(people);
  }

  sortShuffle() {
    this.researchers = this.filterService.sortShuffle(people);
  }

  filterProfiles(event:any) {
    let query: string = event.target.value.toLowerCase();
    this.researchers = this.filterService.filterProfiles(query, people);
  }


  filterInterests() {
    this.researchers = this.filterService.filterInterests(people, this.rinterests);
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
