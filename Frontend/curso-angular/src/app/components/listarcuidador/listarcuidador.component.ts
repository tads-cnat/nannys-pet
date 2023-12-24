import { Component } from '@angular/core';
import { Cuidador } from '../../Cuidador';
import { CuidadorService } from '../../services/cuidador.service';

@Component({
  selector: 'app-listarcuidador',
  templateUrl: './listarcuidador.component.html',
  styleUrl: './listarcuidador.component.css'
})
export class ListarcuidadorComponent {
  cuidadors: Cuidador[] = [];
  cuidador: Cuidador = {id:1,nome:'',sobrenome:'',cpf:'', email:'', endereco:'',telefone:''};
  whatsapp: string= 'https://wa.me/';
  
  constructor(private service: CuidadorService){}
  
  ngOnInit() {
    this.service.getCuidadors().subscribe( data => this.cuidadors = data);
  }

}
