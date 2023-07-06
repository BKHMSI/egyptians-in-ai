import { Component, ViewEncapsulation, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RoutesRecognized  } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class AppComponent implements OnInit {
  title = 'Egyptians in AI';
  en_active: boolean = true;
  
  constructor(private route: ActivatedRoute, private router: Router) {

  }

  ngOnInit(): void {
      this.router.events.subscribe(val => {
          if (val instanceof RoutesRecognized) {
              let lang = val.url.slice(1);
              this.changeLang(lang);
          }
      });
  }

  changeLang(lang: string): void {
    if(lang == "ar")
      this.en_active = false;
    else
      this.en_active = true;
  }

}
