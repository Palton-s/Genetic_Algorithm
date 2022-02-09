       FUNCTION ran4(idum)
	 INTEGER idum
         REAL ran4
         INTEGER idums,irword,itemp,jflmsk,jflone,lword
         REAL ftemp
         EQUIVALENCE (itemp,ftemp)
         SAVE idums,jflone,jflmsk
         DATA idums /0/,jflone /Z'3F800000'/,jflmsk /Z'007FFFFF'/
         IF(idum .LT. 0)THEN
            idums=idum
            idum=1
         END IF
         irword=idum
         lword=idums
         CALL psdes(lword,iword)
         itemp=ior(jflone,iand(jflmsk,irword))
         ran4=ftemp-1.0d0
         idum=idum+1
         RETURN	
       END

       PROGRAM random4
	IMPLICIT REAL*8(A-H,O-Z)
	REAL ran4
	DO I=1,100
	 !idum=I
         Z=ran4(idum)
	 PRINT*,Z
        END DO
       END
       
       SUBROUTINE psdes(lword,irword)
         INTEGER irword,lword,NITER			 
	 PARAMETER (NITER=4)
         INTEGER i,ia,ib,iswap,itmph,itmpl,c1(4),c2(4)
	 SAVE c1,c2
         DATA c1 /Z'BAA96887',Z'1E17D32C',Z'03BCDC3C',Z'0F33D1B2'/ 
	 DATA c2 /Z'4B0F3B58',Z'E874F0C3',Z'6955C5A6',Z'55A7CA46'/
	 DO i=1,NITER
           iswap=irword
	   ia=ieor(irword,c1(i))
           itmpl=iand(ia,65535)
	   itmph=iand(ishft(ia,-16),65535)
	   ib=itmpl**2+not(itmph**2)
           ia=ior(ishft(ib,16),iand(ishft(ib,-16),65535))
           iword=ieor(lword,ieor(c2(i),ia)+itmpl*itmph)	
	 END DO
	 RETURN
        END
