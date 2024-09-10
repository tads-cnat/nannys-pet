import { Injectable, Inject, PLATFORM_ID } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { tap } from 'rxjs/operators';
import { isPlatformBrowser } from '@angular/common';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseUrl = 'http://127.0.0.1:8000/api/v1/';  // URL da sua API de login
  private loggedIn = new BehaviorSubject<boolean>(false);

  constructor(
    private http: HttpClient,
    @Inject(PLATFORM_ID) private platformId: Object
  ) {
    // Verifica se o usuário já está logado ao iniciar
    if (isPlatformBrowser(this.platformId)) {
      this.loggedIn.next(!!localStorage.getItem('token'));
    }
  }

  // Método para login
  login(username: string, password: string): Observable<any> {
    return this.http.post(this.baseUrl + 'api/login/', { username, password }).pipe(
      tap((response: any) => {
        if (isPlatformBrowser(this.platformId)) {
          // Armazena o token no localStorage e atualiza o estado de login
          localStorage.setItem('token', response.token);
          this.loggedIn.next(true);
        }
      })
    );
  }

  // Método para logout
  logout(): void {
    if (isPlatformBrowser(this.platformId)) {
      localStorage.removeItem('token');
      this.loggedIn.next(false);
    }
  }

  // Verifica se o usuário está logado
  isLoggedIn(): Observable<boolean> {
    return this.loggedIn.asObservable();
  }

  // Obtém o token de autenticação
  getToken(): string | null {
    if (isPlatformBrowser(this.platformId)) {
      return localStorage.getItem('token');
    }
    return null;
  }

  // Método para registro
  register(username: string, password: string): Observable<any> {
    return this.http.post(`${this.baseUrl}register/`, { username, password });
  }

  // Método para definir o token
  setToken(token: string): void {
    if (isPlatformBrowser(this.platformId)) {
      localStorage.setItem('token', token);
    }
  }
}
