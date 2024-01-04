import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RsvpService {
  private apiUrl = 'http://backend:5000/rsvp';  // Update the URL if needed

  constructor(private http: HttpClient) { }

  postRsvp(data: any) {
    return this.http.post(this.apiUrl, data);
  }
}
