import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-cadastro-tutor1',
  templateUrl: './cadastro-tutor1.component.html',
  styleUrl: './cadastro-tutor1.component.css'
})
export class CadastroTutor1Component {
  registroForm: FormGroup;

  constructor(private fb: FormBuilder, private http: HttpClient) {
    this.registroForm = this.fb.group({
      nome: ['', Validators.required],
      sobrenome: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      dataNascimento: ['', Validators.required],
      cpf: ['', Validators.required],
      senha: ['', Validators.required],
      confirmarSenha: ['', Validators.required],
    });
  }
  onSubmit() {
    if (this.registroForm.valid) {
      // Enviar os dados para a API Django REST
      const dados = this.registroForm.value;
      this.http.post('URL_DA_SUA_API', dados).subscribe(
        (response) => {
          console.log('Registro bem-sucedido:', response);
        },
        (error) => {
          console.error('Erro durante o registro:', error);
        }
      );
    }
  }
}

