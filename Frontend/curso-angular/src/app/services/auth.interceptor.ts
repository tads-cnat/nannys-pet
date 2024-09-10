import { Injectable } from '@angular/core';
import { HttpEvent, HttpInterceptor, HttpHandler, HttpRequest } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service'; // Ajuste o caminho conforme necessário

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor(private authService: AuthService) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // Clonando a requisição para adicionar o cabeçalho de autenticação
    let authReq = req;
    const token = this.authService.getToken();

    if (token) {
      authReq = req.clone({
        setHeaders: {
          Authorization: `Bearer ${token}`
        }
      });
    }

    // Passa a requisição para o próximo interceptor (ou para o manipulador de requisições se for o último)
    return next.handle(authReq);
  }
}
