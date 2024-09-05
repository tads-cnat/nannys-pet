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

  constructor(private authService: AuthService, private router: Router) {}

  checkPasswords() {
    // A função para verificar se as senhas coincidem é chamada em tempo real
  }

  onSubmit(f: NgForm) {
    if (this.password !== this.confirmPassword) {
      this.errorMessage = 'As senhas não correspondem.';
      return;
    }

    this.authService.register(this.username, this.password).subscribe(
      (response) => {
        console.log('Usuário cadastrado com sucesso', response);
        this.router.navigate(['/login']); // Redireciona para a página de login após o cadastro
      },
      (error) => {
        console.error('Erro ao cadastrar usuário', error);
        this.errorMessage = 'Erro ao cadastrar usuário. Tente novamente.';
      }
    );
  }
}
