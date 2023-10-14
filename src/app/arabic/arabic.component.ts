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

  editProfile(researcher:IResearcher) {
    let link_template = "https://docs.google.com/forms/d/e/1FAIpQLSdLaYBQyOzI5gnlGzwOki3b1TJtFjLUeHUKxkGtXQDhHdSreg/viewform?usp=pp_url&entry.186050192=Update&entry.1945362270={name}&entry.843703109={affiliation}&entry.1728443742={position}&entry.113990162={gscholar}&entry.1193057171={linkedin}&entry.2083985192={twitter}&entry.1542622457={website}&entry.2030031116={research_interests}"
    link_template = link_template.replace("{name}", researcher.name)
    link_template = link_template.replace("{affiliation}", researcher.affiliation)
    link_template = link_template.replace("{position}", researcher.position)
    link_template = link_template.replace("{gscholar}", researcher.scholar)
    link_template = link_template.replace("{linkedin}", researcher.linkedin)
    link_template = link_template.replace("{twitter}", researcher.twitter)
    link_template = link_template.replace("{website}", researcher.website)
    link_template = link_template.replace("{research_interests}", researcher.interests.join(','))
    window.open(link_template, "_blank")
  }
}
