!EXTREMES OF FUNCTIONS BY GENETICS ALGORITHMS
!DATE:04/09/2008
!LUIZ ANTONIO RINEIRO JUNIOR
       

       PROGRAM teste1
        IMPLICIT REAL*8(A-H,O-Z)
        INCLUDE 'parameters.inc'
        DIMENSION X(NV,N),Y(N),T(N),Son1(NV,N),EliteX(NV,N)
        DIMENSION Probability(N),ProbTrack(N+1),Reproducer(NV,N)
	DIMENSION D(NV),Son2(NV,N),AL(N)
        REAL*4 TARRAY(2)
        
        DO NN=1,NR
          TTIME=123456789.1234
          ITIME=INT(TTIME)
          IF(ITIME .EQ. 0)THEN
           ITIME=ITIME+1
          END IF       
          Random1=RAND()
          Random2=RAND(ITIME)
	  CALL PopulationGenerator(X)
          CALL Printing(X,Y,Icounter,NN)
        END DO 
        END

!************************************************************************
!                       SUBROUTINE POPULATION GENERATOR

       SUBROUTINE PopulationGenerator(X)
         IMPLICIT REAL*8(A-H,O-Z)
         INCLUDE 'parameters.inc'
         DIMENSION X(NV,N),ValueI(NV),ValueF(NV)
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

! 			SUBROUTINE PRINTING

	SUBROUTINE Printing(X,Y,Icounter,NN)
         IMPLICIT REAL*8(A-H,O-Z)
         INCLUDE 'parameters.inc'
         DIMENSION X(NV,N),Y(N)
         CHARACTER*3 NUMERO
!         PRINT*
!         PRINT*
!         PRINT*,'GERACAO', Icounter
!         PRINT*
!	   WRITE(35,*) , '******GERACAO******', Icounter 
!	   WRITE(35,*) '   '
!	   WRITE(35,*) '   '		
!         DO I=1,N
	   L=1	
	   WRITE(*,11) X(L,N),X(L+1,N),Y(N)
!	   WRITE(NN,11) Icounter,Y(N)
!      WRITE(NUMERO,*) NN
!      OPEN(15,ACCESS='APPEND',FILE=NUMERO//'.txt',FORM='FORMATTED')
!	WRITE(15,11) Icounter,Y(N) 
!        CALL FLUSH(15)
!      CLOSE(15,STATUS='KEEP') 
!	   WRITE(35,11) X(L,I),X(L+1,I),Y(I) 
11        FORMAT(F5.3,T10,F5.3,T20,F5.3)
!11         FORMAT(I7,T10,F12.9)
!         END DO
         RETURN
       END

