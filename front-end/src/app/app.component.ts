import { Component } from '@angular/core';
import { faRepublican, faDemocrat, faFire, faVoteYea } from '@fortawesome/free-solid-svg-icons';
import { VoteService } from 'src/_service/vote.service';
import { Vote } from 'src/_model/vote';


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

  selectedParty: string;
  voteRequest : Vote = new Vote();
  loading: boolean = false;
  votingSuccessful: boolean = false;

  constructor(private voteService: VoteService) {

  }

  ngOnInit() { }

  setVote(party: string) {
    this.selectedParty = party;
    switch(party) {
      case 'DEMOCRATS':
        this.voteRequest.vote = "DEMOCRATS";
        this.voteRequest.vote_id = 1;
        break;

      case 'REPUBLICANS':
        this.voteRequest.vote = "REPUBLICANS";
        this.voteRequest.vote_id = 2;
        break;

      case 'PROTEST':
        this.voteRequest.vote = "PROTEST";
        this.voteRequest.vote_id = 3;
        break;
    }

  }
  castVote() {
    // check if its odd
    this.loading = true;
    let oddOrEven = this.voteRequest.id % 2;

    // call API based on odd/even ID
    this.voteService.castVote(oddOrEven, this.voteRequest).subscribe(
      response => {
        console.log(response);
        if (response.success === true) {
          this.votingSuccessful = true;
        }

        this.loading = false;
      }
    )
  }

}
