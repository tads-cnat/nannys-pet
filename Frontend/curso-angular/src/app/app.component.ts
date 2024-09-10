import { Router, NavigationEnd } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { AuthService } from './services/auth.service';
import { filter } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  isLoginPage: boolean = false;
  isLoggedIn: boolean = false;
  constructor(private authService: AuthService, private router: Router) {}

  ngOnInit(): void {
    this.authService.isLoggedIn().subscribe((loggedIn) => {
      this.isLoggedIn = loggedIn;
    });
    this.router.events
      .pipe(
        filter(event => event instanceof NavigationEnd)
      )
      .subscribe(() => {
        this.isLoginPage = this.router.url === '/login';
      });
  }

  toggleAuth(): void {
    if (this.isLoggedIn) {
      this.authService.logout();
    } else {
      this.router.navigate(['/login']);
    }
  }
  logout(): void {
    this.authService.logout();
    this.router.navigate(['/login']);
  }
  
}

