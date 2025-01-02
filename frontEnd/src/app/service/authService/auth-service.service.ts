import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {

  private authUrl = 'http://127.0.0.1:8000/auth';
  private isLoggedInSubject: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(this.isLoggedIn());


  constructor(private http: HttpClient) { }

  // Funcao para criar nova conta
  register(username: string, email: string, password: string): Observable<any> {
    let body = { email, username, password }
    return this.http.post(`${this.authUrl}/users/`, body)
  }

  // Função para fazer login e obter o token
  login(username: string, password: string): Observable<any> {
    const body = { username, password }
    return this.http.post(`${this.authUrl}/token/login/`, body);
  }

  // Função para guardar o token no localStorage
  storeToken(token: string) {
    localStorage.setItem('auth_token', token);
    this.isLoggedInSubject.next(true);
  }

  // Função para obter o token do localStorage
  getToken() {
    return localStorage.getItem('auth_token')
  }

  // Função para adicionar o token ao header das requisições
  getHeaders() {
    const token = this.getToken();
    return token ? new HttpHeaders().set('Authorization', `Token ${token}`) : new HttpHeaders();
  }

  // Função para logout (limpar token)
  logout() {
    localStorage.clear()
    this.isLoggedInSubject.next(false);
  }
  // Função para verificar se o usuário está logado
  isLoggedIn(): boolean {
    return !!this.getToken(); // Verifica se o token existe
  }

  // Observable para saber o estado de login
  hasLogin$ = this.isLoggedInSubject.asObservable();

}
