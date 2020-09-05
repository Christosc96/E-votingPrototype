import { Injectable } from '@angular/core';
import { Vote } from 'src/_model/vote';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import {map} from 'rxjs/operators';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class VoteService {

  constructor(private http: HttpClient) { }

  castVote(oddOrEven: number, voteReq : Vote) : Observable<any> {
    
    let url;
    oddOrEven === 0 
    ? url = environment.serverUrl + environment.cast_vote_even
    : url = environment.serverUrl + environment.cast_vote_odd;
    
    return this.http.post(url, voteReq).pipe(
      map( response => {
        return <any> response;
      })
    )

  }
}
