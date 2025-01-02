import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthServiceService } from '../../service/authService/auth-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cadastro',
  standalone: true,
  imports: [
    FormsModule,
  ],
  templateUrl: './cadastro.component.html',
  styleUrl: './cadastro.component.css'
})
export class CadastroComponent {

  usuario: string = ''
  email: string = ''
  senha: string = ''
  senha2: string = ''
  alerta: string = ''

  constructor(
    private _authServiceService: AuthServiceService,
    private _Router: Router,
  ) { }

  cadastro() {
    this._authServiceService.register(this.usuario, this.email, this.senha).subscribe(
      (response) => {
        alert('Cadastro realizado com sucesso')
        this._Router.navigate(['login'])
      },
      (error) => { this.alerta = error.error.error.message }
    )

  }

}
