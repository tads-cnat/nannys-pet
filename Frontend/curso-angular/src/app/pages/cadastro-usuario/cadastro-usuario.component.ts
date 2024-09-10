import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cadastro-usuario',
  templateUrl: './cadastro-usuario.component.html',
  styleUrls: ['./cadastro-usuario.component.css']
})
export class CadastroUsuarioComponent {
  username: string = '';
  password: string = '';
  confirmPassword: string = '';
  errorMessage: string | null = null;
  successMessage: string | null = null;
  isSubmitted: boolean = false;

  constructor(private authService: AuthService, private router: Router) {}

  checkPasswords() {
    if (this.password !== this.confirmPassword) {
      this.errorMessage = 'As senhas não correspondem.';
    } else {
      this.errorMessage = null;
    }
  }

  registerUser(): void {
    this.authService.register(this.username, this.password).subscribe(
      (response: any) => {
        console.log('Usuário cadastrado com sucesso', response);
        this.successMessage = 'Usuário cadastrado com sucesso!';
        this.isSubmitted = true;
      },
      (error: any) => {
        console.error('Erro ao cadastrar usuário', error);
        this.errorMessage = 'Erro ao cadastrar usuário. Tente novamente.';
      }
    );
  }

  onSubmit(f: NgForm) {
    if (this.password !== this.confirmPassword) {
      this.errorMessage = 'As senhas não correspondem.';
      return;
    }
    this.registerUser();
  }
}
