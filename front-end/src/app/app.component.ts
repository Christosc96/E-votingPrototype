import { Component } from '@angular/core';
import { faRepublican, faDemocrat, faFire, faVoteYea } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent { 
  faRepublican = faRepublican;
  faDemocrat = faDemocrat;
  faFire = faFire;
  faVoteYea = faVoteYea;
}
