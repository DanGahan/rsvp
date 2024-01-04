import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-rsvp-form',
  templateUrl: './rsvp-form.component.html',
  styleUrls: ['./rsvp-form.component.css']
})
export class RsvpFormComponent implements OnInit {
  name: string = '';
  plusOne: string = '';
  plusOneName: string = '';
  songSuggestion: string = '';

  constructor() { }

  ngOnInit(): void {
  }

  submitForm(): void {
    // Handle form submission logic here
    console.log('Form submitted:', this.name, this.plusOne, this.plusOneName, this.songSuggestion);
    // You can add code here to send the form data to the backend API
  }
}
