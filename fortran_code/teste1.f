!EXTREMES OF FUNCTIONS BY GENETICS ALGORITHMS
!DATE:04/09/2008
!LUIZ ANTONIO RINEIRO JUNIOR
       

       PROGRAM teste1
        IMPLICIT REAL*8(A-H,O-Z)
        INCLUDE 'parameters.inc'
        REAL*4 TARRAY(2)	
	COMMON X(NV,N),Y(N),T(N),Son1(NV,N),EliteX(NV,N)
	COMMON Probability(N),ProbTrack(N+1),Reproducer(NV,N)
	COMMON D(NV),Son2(NV,N),AL(N)        
 
        DO NN=1,NR
!          TTIME=ETIME(TARRAY)
!          ITIME=INT(TTIME)
!          IF(ITIME .EQ. 0)THEN
!           ITIME=ITIME+1
!          END IF       
          Random1=RAND()
          Random2=RAND(1)
	  CALL PopulationGenerator()
	   DO Icounter=1,Igeneration
            CALL Evaluation()
	    PRINT*, 'ORDEM SHELL'
            CALL Ordering2()
	    TTIME=ETIME(TARRAY)
	    PRINT*, TTIME
!	    CALL Printing(Icounter,NN)
	    PRINT*
	    PRINT*
	    PRINT*, 'ORDEM BOBLLE' 
           CALL Ordering1()
            TTIME=ETIME(TARRAY)
	    PRINT*, TTIME	
!	    CALL Printing(Icounter,NN)
!	    TTIME=ETIME(TARRAY)
!            PRINT*,TTIME
!            CALL Printing(Icounter,NN)
!           CALL Translation()
!	    CALL ALine()
!            CALL Track()
!            CALL Selection()
!	    CALL Deviation()	
!            CALL Gaussian(K)
!            CALL Attribution()
!	    CALL Mutation(Icounter)
!            CALL Elitism()
          END DO
        END DO 
        END

!************************************************************************
!                       SUBROUTINE POPULATION GENERATOR

       SUBROUTINE PopulationGenerator()
         IMPLICIT REAL*8(A-H,O-Z)
         INCLUDE 'parameters.inc'
         DIMENSION ValueI(NV),ValueF(NV)
         COMMON X(NV,N)
         DO I=1,NV
	    READ(10,*),ValueI(I),ValueF(I)
	 END DO
         REWIND 10
	 DO I=1,NV
            DO J=1,N
               W=RAND()
               X(I,J)=(ValueF(I)-ValueI(I))*W+ValueI(I)
            END DO
	 END DO 
         RETURN
        END
!************************************************************************

!************************************************************************
!                       SUBROUTINE EVALUATION

       SUBROUTINE Evaluation()
         IMPLICIT REAL*8(A-H,O-Z)
         INCLUDE 'parameters.inc'
!        DIMENSION Z(100)            !PARA FUNCAO TESTE 4
         COMMON X(NV,N),Y(N)
	 I=1
	 w=9.0d0
	 s=0.15d0
	 pi=3.141592d0
!	 A1=0.9d0
!	 A2=0.3d0
!	 A3=0.1d0
!	 A4=0.3d0
!	 A5=0.8d0
!	 A6=0.025d0
	 DO J=1,N
!         Funcao Teste 1
          r=((X(I,J)-0.5d0)**2+(X(I+1,J)-0.5d0)**2)
          Y(J)=(DCOS(w*pi*r))**2*exp(-(r/s))

!	  Funcao Teste 2
!	   ra=((X(I,J)-0.5d0)**2+(X(I+1,J)-0.5d0)**2)
!	   rb=((X(I,J)-0.6d0)**2+(X(I+1,J)-0.1d0)**2)
!          A=exp((-1.0d0)*ra/(0.3d0**2))
!	   B=exp((-1.0d0)*rb/(0.03d0**2)) 
!	   Y(J)=0.8d0*A+0.879008d0*B

!	  Funcao Teste 3
!           ra=((X(I,J)-0.5d0)**2+(X(I+1,J)-0.5d0)**2)
!	   rb=((X(I+2,J)-0.5d0)**2+(X(I+3,J)-0.5d0)**2)
!	   r=ra+rb	
!           Y(J)=(DCOS(w*pi*r))**2*exp(-(r/s))

!         Funcao Teste 4
!	   DO M=1,100
!	      Z(M)=0.01*M	
!	   END DO
!	   Sum=0.0d0
!	   DO L=1,100
!	    ra=(Z(L)-A2)**2/(A3)**2   
!	    rb=(Z(L)-A5)**2/(A6)**2
!	    F1=A1*exp(-ra)+A4*exp(-rb)
!	    rc=(Z(L)-X(I,J))**2/(X(I+1,J))**2   
!	    rd=(Z(L)-X(I+2,J))**2/(X(I+3,J))**2
!	    F2=X(I+4,J)*exp(-rc)+X(I+5,J)*exp(-rd)
!	    Sum=Sum+(F2-F1)**2	
!	   END DO
!	   Y(J)=(-1.0d0)*Sum	
         END DO
         RETURN
       END
!************************************************************************

!************************************************************************
!                       SUBROUTINE ORDERING1

       SUBROUTINE Ordering1()
         IMPLICIT REAL*8(A-H,O-Z)
         INCLUDE 'parameters.inc'
	 COMMON X(NV,N),Y(N),EliteX(NV,N)
         DO I=(N-1),1,-1
            DO J=1,(N-1)	
               IF(Y(J) .GT. Y(J+1))THEN
                 AuxiliaryY=Y(J)
                 Y(J)=Y(J+1)
                 Y(J+1)=AuxiliaryY
		 DO L=1,NV
                   AuxiliaryX=X(L,J)
                   X(L,J)=X(L,J+1)
                   X(L,J+1)=AuxiliaryX
		 END DO
	       END IF  
            END DO
         END DO
!	 DO I=1,N
!           PRINT*, Y(I)
!        END DO
	 MM=INT(N*0.01)
	 DO J=(N-MM),N
	   DO I=1,NV
	     EliteX(I,J)=X(I,J)
	   END DO	
	 END DO
         RETURN
       END
!************************************************************************

!************************************************************************
!                       SUBROUTINE ORDERING2

       SUBROUTINE Ordering2()
         IMPLICIT REAL*8(A-H,O-Z)
         INCLUDE 'parameters.inc'
	 DIMENSION VX(NV)
         COMMON X(NV,N),Y(N),EliteX(NV,N)
	 INC=1
    	 DO WHILE(INC .LE. N)
	    INC=3*INC+1
	 END DO	
	 DO WHILE(INC .GT. 1)	
	    INC=INC/3
            do I=INC+1,N
		VY=Y(i)
		DO LI=1,NV
                  VX(LI)=X(LI,I)
                END DO
		J=I
	    DO WHILE(Y(J-INC) .gt. VY)
	       Y(J)=Y(J-INC)
	       DO LJ=1,NV
                 X(LJ,J)=X(LJ,J-INC)
               END DO
	       J=J-INC
	       IF(J .LE. INC)EXIT	
	    END DO
           Y(J)=VY
           DO LK=1,NV
             X(LK,J)=VX(LK)
           END DO
	   END DO
	 END DO   
!	 DO II=1,N
!	   PRINT*, Y(II)
!	 END DO	
!        MM=INT(N*0.01)
!        DO J=(N-MM),N
!          DO I=1,NV
!            EliteX(I,J)=X(I,J)
!          END DO
!        END DO
         RETURN
       END
!************************************************************************

!************************************************************************
! 			SUBROUTINE PRINTING

	SUBROUTINE Printing(Icounter,NN)
         IMPLICIT REAL*8(A-H,O-Z)
         INCLUDE 'parameters.inc'
         COMMON X(NV,N),Y(N)
         CHARACTER*3 NUMERO
!         PRINT*
!         PRINT*
!         PRINT*,'GERACAO', Icounter
!         PRINT*
!	   WRITE(35,*) , '******GERACAO******', Icounter 
!	   WRITE(35,*) '   '
!	   WRITE(35,*) '   '		
!         DO I=1,N
!	   L=1	
!	   WRITE(*,11) X(L,I),X(L+1,I),Y(I)
!	   WRITE(NN,11) Icounter,Y(N)
	   WRITE(*,11) Icounter,Y(N)
!        WRITE(NUMERO,*) NN
!        OPEN(15,ACCESS='APPEND',FILE=NUMERO//'.txt',FORM='FORMATTED')
!	WRITE(15,11) Icounter,Y(N) 
!        CALL FLUSH(15)
!       CLOSE(15,STATUS='KEEP') 
!	   WRITE(35,11) X(L,I),X(L+1,I),Y(I) 
!11        FORMAT(F5.3,T10,F5.3,T20,F5.3)
11         FORMAT(I7,T10,F6.4)
!         END DO
         RETURN
       END
!************************************************************************

!************************************************************************
!                      SUBROUTINE TRANSLATION

      SUBROUTINE Translation()
        IMPLICIT REAL*8(A-H,O-Z)
        INCLUDE 'parameters.inc'
	COMMON Y(N),T(N)
        DO I=1,N
          T(I)=Y(I)-Y(1)
        END DO
        RETURN
      END

!************************************************************************

!************************************************************************
!			SUBROUTINE ALINE
       SUBROUTINE ALine()
	IMPLICIT REAL*8(A-H,O-Z)
	INCLUDE 'parameters.inc'
        COMMON T(N),AL(N)
	Sum=0.0d0
	DO I=1,N
	   Sum=Sum+T(I)
	END DO
	Copy=1.2d0
	AverageT=Sum/(N*1.0d0)
	A=((Copy-1.0d0)*AverageT)/(T(N)-AverageT)
	B=(1.0d0-A)*AverageT
	DO I=1,N
	  AL(I)=A*T(I)+B
	END DO
	DO I=1,N
	  WRITE(60,*) T(I),AL(I)
	END DO
       END	
!************************************************************************


!************************************************************************
!                       SUBROUTINE TRACK

      SUBROUTINE Track()
         IMPLICIT REAL*8(A-H,O-Z)
         INCLUDE 'parameters.inc'
         COMMON T(N),Probability(N),ProbTrack(N+1)
         Sum=0.0d0
         DO I=1,N
           Sum=Sum+T(I)
         END DO
         DO I=1,N
           Probability(I)=T(I)/Sum
         END DO
	 Auxiliary=0.0d0
	 Probtrack(1)=0.0d0
         DO I=2,(N+1)
           ProbTrack(I)=Auxiliary+Probability(I-1)
           Auxiliary=ProbTrack(I)
         END DO
        RETURN
      END
!************************************************************************

!************************************************************************
!                       SUBROUTINE SELECTION

      SUBROUTINE Selection()
         IMPLICIT REAL*8(A-H,O-Z)
         INCLUDE 'parameters.inc'
	 COMMON X(NV,N),ProbTrack(N+1),Reproducer(NV,N)
	 DO I=1,(N/2)+1
           DO J=1,N
	      Z=RAND()
              IF(ProbTrack(J+1).GT. Z .AND. ProbTrack(J) .LE. Z)THEN
              	DO L=1,NV
		  Reproducer(L,I)=X(L,J)
	        END DO	 
              END IF		
           END DO
	 END DO
	 RETURN 
        END
!************************************************************************

!************************************************************************
!			SUBROUTINE DEVIATION	

	SUBROUTINE Deviation()
	   IMPLICIT REAL*8(A-H,O-Z)
	   INCLUDE 'parameters.inc'
	   COMMON X(NV,N),D(NV)
	   DO I=1,NV
	     DO J=1,N
	       Sum1=Sum1+X(I,J)
	     END DO
	     AverageD=Sum1/N
	     Sum2=0.0d0	
	     DO L=1,N
	       Sum2=Sum2+(X(I,L)-AverageD)**2
	     END DO
	     D(I)=SQRT(Sum2/N)					
	   END DO
	   RETURN			
	END
!************************************************************************

!************************************************************************
!                       SUBROUTINE GAUSSIAN

       SUBROUTINE Gaussian(K)
         IMPLICIT REAL*8(A-H,O-Z)
         INCLUDE 'parameters.inc'
	 COMMON X(NV,N),Son1(NV,N),Reproducer(NV,N),D(NV),Son2(NV,N)
         DO L=1,NV
	   DO K=2,(N/2)+1
             Walker1=Reproducer(L,K-1)
	     Walker2=Reproducer(L,K)
             Step=D(L)/(2*SQRT(N*1.0d0))
	     Nsteps=100
             IF(Step .LT. 0)THEN
               Step=Step*(-1.0d0)
             END IF
             DO I=1,Nsteps
               W=RAND()
               Q=RAND()*Step
               IF(W .LE. 0.5d0)THEN
                 Walker1=Walker1+Q
               ELSE
                 Walker1=Walker1-Q
               END IF
	     END DO
	     DO I=1,Nsteps
               W=RAND()
               Q=RAND()*Step
               IF(W .LE. 0.5d0)THEN
                 Walker2=Walker2+Q
               ELSE
                 Walker2=Walker2-Q
               END IF
	     END DO
	     Son1(L,K)=Walker1	
	     Son2(L,K)=Wlaker2
	    END DO
          END DO
         RETURN
       END
!***********************************************************************

!**********************************************************************
!                       SUBROUTINE MUTATION

       SUBROUTINE Mutation(Icounter)
         IMPLICIT REAL*8(A-H,O-Z)
         INCLUDE 'parameters.inc'
	 DIMENSION VI(1),VF(1)
	 COMMON X(NV,N)
         READ(10,*),VI(1),VF(1)
         REWIND 10
	 R=(VF(1)-VI(1))*0.01
         M=INT(N*0.01d0)
	 L=1	
         DO I=(N-M+1),N
           W=RAND()
           Auxiliary=W*N
           ChosenMutation=INT(Auxiliary)
           DO WHILE(Auxiliary .EQ. 0.0d0)
              W=RAND()
              Auxiliary=W*N
              ChosenMutation=INT(Auxiliary)
           END DO
           IF(W .GE. 0.5d0)THEN
             X(1,I)=X(1,ChosenMutation)-R
           ELSE
             X(1,I)=X(1,ChosenMutation)+R
           END IF
           X(1,L)=X(1,I)
           L=L+1
         END DO
         RETURN
       END
!***********************************************************************

!***********************************************************************
!                       SUBROUTINE ATTRIBUTION

      SUBROUTINE Attribution()
        IMPLICIT REAL*8(A-H,O-Z)
        INCLUDE 'parameters.inc'
        COMMON X(NV,N),Son2(NV,N),Son1(NV,N)
	DO L=1,NV
	   DO I=1,(N/4)
              X(L,I)=Son1(L,I+1)
	   END DO
        END DO
	DO L=1,NV
	   DO I=((N/4)+1),((N/2)+1)
	       X(L,I)=Son2(L,I)
	   END DO
	END DO
	RETURN
       END
!***********************************************************************

!***********************************************************************
!                       SUBROUTINE ELITISM

       SUBROUTINE Elitism()
        IMPLICIT REAL*8(A-H,O-Z)
        INCLUDE 'parameters.inc'
        COMMON X(NV,N),EliteX(NV,N)
	MM=INT(N*0.01)
        DO J=(N-MM),N
           DO I=1,NV
             X(I,J)=EliteX(I,J)
           END DO
        END DO
	RETURN
       END
!***********************************************************************


