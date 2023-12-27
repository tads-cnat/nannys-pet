import { Injectable } from '@angular/core';
import { HttpHeaders,HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { RespostaCep } from '../RespostaCep';
import { map } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class CepServiceService {

  private apiUrl = 'https://h-apigateway.conectagov.estaleiro.serpro.gov.br/api-cep/v1/consulta/cep/'


  constructor( private http: HttpClient) { }

  obterCidadePorCEP(cep: string, tokenJwt: string): Observable<any>{
    const urlApiCep = `${this.apiUrl}/${cep}`;

    const headers = new HttpHeaders({
      'Authorization': `Bearer ${tokenJwt}`
    });

    return this.http.get<RespostaCep>(urlApiCep, {headers}).pipe(
      map(resposta => resposta.cidade)
    );
  }
}
